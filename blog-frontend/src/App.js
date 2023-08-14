import React, { useState, useEffect } from 'react';
import './App.css';

window.addEventListener('unhandledrejection', (event) => {
    console.error('Unhandled promise rejection:', event.promise, event.reason);
});

function App() {
  const [blogs, setBlogs] = useState([]);
  const [newTitle, setNewTitle] = useState('');
  const [newContent, setNewContent] = useState('');
  const [showInput, setShowInput] = useState(false);
  const handleNewBlogClick = () => {
    setShowInput(!showInput);
  };



  useEffect(() => {
  fetch("https://teds-blogs-9c73db19cf47.herokuapp.com/api/blogs")
    .then(res => {
      if (!res.ok) {
        throw new Error(`Server responded with status: ${res.status}`);
      }
      return res.json();
    })
    .then(data => setBlogs(data))
    .catch(error => {
      console.error("Failed to fetch blogs:", error);
    });
}, []);


  return (
    <div className="App">
      <button className="create-blog-btn" onClick={handleNewBlogClick}>Create a new blog</button>

      {showInput && (
        <div className="input-section">
          <input type="text" placeholder="Title" />
          <textarea placeholder="Content"></textarea>
          <button>Add Blog</button>
        </div>
      )}

      {blogs.map(blog => (
        <div key={blog.id}>
          <h2>{blog.title}</h2>
          <p>{blog.content}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
