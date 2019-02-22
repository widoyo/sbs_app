# jenis obat
DROP TABLE if EXISTS obat;
CREATE TABLE obat (
    id INTEGER PRIMARY KEY autoincrement,
    nama VARCHAR(50) NOT NULL,
    kemasan VARCHAR(35),
    satuan VARCHAR(35),
    c_id INTEGER,
    m_id INTEGER,
    c_date DATETIME default NOW(),
    m_date DATETIME
);

# Stok tiap barang
DROP TABLE if EXISTS stock;
CREATE TABLE stock (
    id INTEGER PRIMARY KEY autoincrement,
    obat_id INTEGER,
    m_date DATETIME default NOW(),
);

# keluar masuk obat
DROP TABLE if EXISTS mutasi;
CREATE TABLE mutasi (
    id INTEGER PRIMARY KEY autoincrement,
    obat_id INTEGER NOT NULL,
    waktu DATETIME DEFAULT NOW(),
# MINUS jika keluar
    banyak INTEGER DEFAULT 1, 
    pihak text,
    c_id INTEGER,
    m_id INTEGER,
    c_date DATETIME default NOW(),
    m_date DATETIME
);


