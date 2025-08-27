"use client";

import { useState, useEffect } from "react";
import { getPosts, createPost, deletePost, getUsers } from "../../services/api";

interface PostForm {
  title: string;
  content: string;
  author: number; 
}

interface User {
  id: number;
  username: string;
}

interface Post {
  id: number;
  title: string;
  content: string;
  author: User;
  created_at: string;
  comments: Comment[];
}

interface Comment {
  id: number;
  author: string;
  text: string;
  created_at: string;
}

export default function PostsPage() {
  const [form, setForm] = useState<PostForm>({ title: "", content: "", author: 0 });
  const [posts, setPosts] = useState<Post[]>([]);
  const [users, setUsers] = useState<{ id: number; username: string }[]>([]);

  useEffect(() => {
    getPosts().then(setPosts).catch(err => console.error(err));
    getUsers().then(setUsers).catch(err => console.error(err));
  }, []);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    await createPost(form);
    setForm({ title: "", content: "", author: 0 });
    getPosts().then(setPosts);
  };

  const handleDelete = async (id: number) => {
    await deletePost(id);
    getPosts().then(setPosts);
};

console.log(users);
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Blog Posts</h1>
      <form onSubmit={handleSubmit} className="mb-6 space-y-2">
        <input
          type="text"
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border p-2 w-full"
          required
        />
        <textarea
          placeholder="Content"
          value={form.content}
          onChange={(e) => setForm({ ...form, content: e.target.value })}
          className="border p-2 w-full"
          required
        />
        <select
          value={form.author}
          onChange={(e) => setForm({ ...form, author: Number(e.target.value) })}
          className="border p-2 w-full"
          required
        >
          <option value="">Pilih Author</option>
          {users.map(user => (
            <option key={user.id} value={user.id}>{user.username}</option>
          ))}
        </select>
        <button className="bg-blue-500 text-white px-4 py-2 rounded">Add Post</button>
      </form>

      <ul>
        {posts.map((post) => (
          <li key={post.id} className="border p-2 mb-4 rounded">
            <button
                onClick={() => handleDelete(post.id)}
                className="text-red-600 hover:underline"
                >
                Hapus
            </button>
            <h2 className="font-bold">{post.title}</h2>
            <p>{post.content}</p>
            <h2 className="font-bold text-teal-400">{post.author.username}</h2>
            <small>{new Date(post.created_at).toLocaleString()}</small>

            {post.comments?.length > 0 && (
              <ul className="pl-4 mt-2 border-l">
                {post.comments.map((c: Comment) => (
                  <li key={c.id}>
                    <b>{c.author}</b>: {c.text} <small>({new Date(c.created_at).toLocaleString()})</small>
                  </li>
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
