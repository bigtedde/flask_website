import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    fetch("https://teds-blogs-9c73db19cf47.herokuapp.com")
      .then(res => res.json())
      .then(data => setBlogs(data));
  }, []);

  return (
    <div className="App">
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
