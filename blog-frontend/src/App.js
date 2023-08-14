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
  const handleShowForm = () => {
    setShowInput(!showInput);
  };


  function addNewBlog() {
      fetch("https://teds-blogs-9c73db19cf47.herokuapp.com/api/blogs", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: newTitle,
          content: newContent
        })
      })
//      .then(res => {
//        console.log('Raw Response:', res);
//        return res.text();  // <-- use text() first for debugging
//      })
//      .then(text => {
//        console.log('Response Text:', text);
//        // Then you can manually try converting it to JSON
//        const data = JSON.parse(text);
//      })
      .then(res => res.json())
      .then(newBlog => {
        setBlogs(prevBlogs => [...prevBlogs, newBlog]);
        // Reset the input fields after adding the new blog
        setNewTitle('');
        setNewContent('');
        setShowInput(false);
      })
      .catch(error => {
        console.error("Error adding blog:", error);
      });
  }


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
      <button className="create-blog-btn" onClick={handleShowForm}>Create a new blog</button>

      {showInput && (
        <div className="input-section">
          <input type="text" placeholder="Title" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} />
          <textarea placeholder="Content" value={newContent} onChange={(e) => setNewContent(e.target.value)}></textarea>
          <button onClick={addNewBlog}>Add Blog</button>
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
