"use client";

import { useEffect, useState } from "react";
import { getBooks, createBook, deleteBook } from "../../services/api";

interface Book {
  id: number;
  title: string;
  author: string;
  published_date: string;
}

interface BookForm {
  title: string;
  author: string;
  published_date: string;
}

export default function BooksPage() {
  const [books, setBooks] = useState<Book[]>([]);
  const [form, setForm] = useState<BookForm>({ title: "", author: "", published_date: "" });

  // ambil data dari API
  useEffect(() => {
    getBooks().then(setBooks);
  }, []);

  // tambah buku
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    await createBook(form);
    setForm({ title: "", author: "", published_date: "" });
    getBooks().then(setBooks);
  };

  // hapus buku
  const handleDelete = async (id: number) => {
    await deleteBook(id);
    getBooks().then(setBooks);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">📚 Daftar Buku</h2>
      <form onSubmit={handleSubmit} className="space-y-2 mb-4">
        <input
          type="text"
          placeholder="Judul"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border p-2 w-full"
          required
        />
        <input
          type="text"
          placeholder="Penulis"
          value={form.author}
          onChange={(e) => setForm({ ...form, author: e.target.value })}
          className="border p-2 w-full"
          required
        />
        <input
          type="date"
          value={form.published_date}
          onChange={(e) => setForm({ ...form, published_date: e.target.value })}
          className="border p-2 w-full"
          required
        />
        <button type="submit" className="bg-blue-500 text-white px-3 py-1 rounded">
          Tambah
        </button>
      </form>

      <ul className="space-y-2">
        {books.map((b) => (
          <li key={b.id} className="flex justify-between border p-2 rounded">
            <span>{b.title} - {b.author} ({b.published_date})</span>
            <button
              onClick={() => handleDelete(b.id)}
              className="text-red-600 hover:underline"
            >
              Hapus
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
