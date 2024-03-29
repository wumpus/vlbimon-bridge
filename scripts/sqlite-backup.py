import sys
import sqlite3

src = sys.argv[1]
dest = sys.argv[2]

src_con = sqlite3.connect(src)
src_cur = src_con.cursor()

print('starting merge of the WAL (write ahead log)')
src_cur.execute('PRAGMA wal_checkpoint(TRUNCATE)')
src_con.commit()
print(' finished')

# at this point the WAL ?might? re-appear, but its size will be minimized

dest_con = sqlite3.connect(dest)
dest_cur = dest_con.cursor()

print('starting backup')
src_con.backup(dest_con)

src_con.close()
dest_con.close()
print(' finished')
