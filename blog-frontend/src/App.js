import React, { useState, useEffect } from 'react';
import BlogList from './components/BlogList';
import NewBlogForm from './components/NewBlogForm';
import { fetchBlogs, addBlog, updateBlogInAPI } from './services/blogService';
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

  const handleUpdateBlog = (blogId, newTitle, newContent) => {
    updateBlogInAPI(blogId, newTitle, newContent)
      .then(updatedBlog => {
        setBlogs(prevBlogs => {
          // Find the index of the blog you've updated
          const blogIndex = prevBlogs.findIndex(blog => blog.id === updatedBlog.id);

          // Check if the blog was found
          if (blogIndex === -1) {
            return prevBlogs; // If not found, return the original array
          }

          // Use the spread operator to make a new array with the updated blog
          return [
            ...prevBlogs.slice(0, blogIndex),
            updatedBlog,
            ...prevBlogs.slice(blogIndex + 1)
          ];
        });
      })
      .catch(error => {
        console.error("Error updating blog:", error);
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
      <header className="app-header">Google Summer of Code 2023 - Weekly Blogs by Ted Lawson
        <button className="create-blog-btn" onClick={handleShowForm}>Create a new blog</button>
        {/* I can put more header objects here in the future*/}
        </header>
      {showInput && <NewBlogForm onNewBlog={handleNewBlog} />}
      <BlogList blogs={blogs} updateBlog={handleUpdateBlog} />
    </div>
  );
}

export default App;
