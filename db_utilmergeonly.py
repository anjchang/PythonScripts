#!/usr/bin/python2

import sqlite3, os, sys
from Crypto.Cipher import DES
from Crypto.Hash import MD5

def is_database(filename):
    """
Check whether this file is a valid funf database.
"""
    # Implementation is kludgy, but this is lifted directly from funf...
    _random_table_name = 'jioanewvoiandoasdjf'
    result = False
    try:
        conn = sqlite3.connect(filename)
        conn.execute('create table {0} (nothing text)'.format(_random_table_name))
        conn.execute('drop table {0}'.format(_random_table_name))
        result = True
    finally:
        if conn is not None: conn.close()
        return result

def decrypt(in_filename, out_filename, password = 'changeme',
            salt = '\xa6\xab\x09\x93\xf4\xcc\xee\x10', iterations = 135):
    """
Decrypt a database file.
"""
    # Imitate java's PBEWithMD5AndDES algorithm to produce a DES key.
    # Lifted from funf with minor simplifications.
    def set_parity(char): # set parity bit of a character
        parity, num = True, ord(char)
        while num: parity, num = not parity, num & (num - 1) # count bits
        return chr(ord(char) ^ parity)
    result = None
    for i in range(iterations):
        hasher = MD5.new()
        hasher.update(result or (password + salt))
        result = hasher.digest()
    decryptor = DES.new(''.join(map(set_parity, result[:8])))
    with open(in_filename, 'rb') as in_file:
        data = decryptor.decrypt(in_file.read())
    with open(out_filename, 'wb') as out_file:
        out_file.write(data)

def merge(in_filenames, out_filename):
    """
Combine several (already-decrypted) database files into one file.
"""
    out_conn = sqlite3.connect(out_filename)
    out_conn.row_factory = sqlite3.Row
    out_cursor = out_conn.cursor()
    out_cursor.execute('create table data (id text, device text, probe text, timestmp long, value text)')
    for in_filename in in_filenames:
        try:
            in_conn = sqlite3.connect(in_filename)
            in_conn.row_factory = sqlite3.Row
            in_cursor = in_conn.cursor()
            in_cursor.execute("select * from file_info")
            id, name, device, uuid, created = next(in_cursor)
            in_cursor.execute("select * from data")
            for id, probe, timestamp, value in in_cursor:
                out_conn.execute("insert into data values (?, ?, ?, ?, ?)",
                                 ('{0}-{1}'.format(uuid, id), device,
                                  probe, timestamp, value))
            out_conn.commit()
        except:
            print("Error merging {0}".format(in_filename))
    out_cursor.close()

if __name__ == '__main__':
    directory = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    outfile = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else './merged.db')
    print("Merging databases in {0}".format(directory))
    dbfiles = []
    for dirpath, dirnames, filenames in os.walk(directory):
        print("Scanning {0}".format(dirpath))
        for filename in filenames:
            if filename.lower().endswith('.db'):
                path = os.path.join(dirpath, filename)
                dbfiles.append(path)
#                if not is_database(path):
#                    decrypt(path, path)
#                if is_database(path):
#                    dbfiles.append(path)
#                else:
                print("Corrupted database {0}".format(path))
    print("Merging databases")
    merge(dbfiles, outfile)
