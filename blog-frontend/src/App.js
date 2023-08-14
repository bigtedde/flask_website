import React, { useState, useEffect } from 'react';
import BlogList from './components/BlogList';
import NewBlogForm from './components/NewBlogForm';
import { fetchBlogs, addBlog } from './services/blogService';
import './App.css';

function App() {
  const [blogs, setBlogs] = useState([]);
  const [showInput, setShowInput] = useState(false);

  const handleShowForm = () => {
    setShowInput(!showInput);
  };

  const handleNewBlog = (title, content) => {
    addBlog(title, content)
      .then(newBlog => {
        setBlogs(prevBlogs => [...prevBlogs, newBlog]);
        setShowInput(false);
      })
      .catch(error => {
        console.error("Error adding blog:", error);
      });
  }

  useEffect(() => {
    fetchBlogs()
      .then(data => setBlogs(data))
      .catch(error => {
        console.error("Failed to fetch blogs:", error);
      });
  }, []);

  return (
    <div className="App">
      <button className="create-blog-btn" onClick={handleShowForm}>Create a new blog</button>
      {showInput && <NewBlogForm onNewBlog={handleNewBlog} />}
      <BlogList blogs={blogs} />
    </div>
  );
}

export default App;
