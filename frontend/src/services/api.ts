const API_BOOKS_URL = "http://127.0.0.1:8000/api/books/";
const API_BLOGS_URL = "http://127.0.0.1:8000/api/blogs/";

type Book = {
  title: string;
  author: string;
}

export async function getBooks() {
  const res = await fetch(`${API_BOOKS_URL}`, { cache: "no-store" });
  const data = await res.json();
  return data.results || data;
  // return res.json();
}

export async function createBook(data: { title: string; author: string; published_date: string }) {
  const res = await fetch(`${API_BOOKS_URL}create`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function updateBook(id: number, data: Book) {
  const res = await fetch(`${API_BOOKS_URL}update/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function deleteBook(id: number) {
  return fetch(`${API_BOOKS_URL}delete/${id}`, { method: "DELETE" });
}

export async function getPosts() {
  const res = await fetch(`${API_BLOGS_URL}posts/`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch posts");
  const data = await res.json();
  return data.results || data;
}

export async function createPost(data: { title: string; content: string; author: number }) {
  const res = await fetch(`${API_BLOGS_URL}posts/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create post");
  const datas = await res.json();
  return datas;
}

export async function deletePost(id: number) {
  return fetch(`${API_BLOGS_URL}posts/${id}/`, { 
    method: "DELETE" 
  });
}

export async function getUsers() {
  const res = await fetch(`${API_BLOGS_URL}users/list`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch posts");
  const data = await res.json();
  return data.results || data;
}