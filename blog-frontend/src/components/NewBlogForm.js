import './NewBlogForm.css';
import React, { useState } from 'react';

function NewBlogForm({ onNewBlog }) {
  const [newTitle, setNewTitle] = useState('');
  const [newContent, setNewContent] = useState('');

  const addNewBlog = () => {
    onNewBlog(newTitle, newContent);
    setNewTitle('');
    setNewContent('');
  }

  return (
    <div className="input-section">
      <input type="text" placeholder="Title" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} />
      <textarea placeholder="Content" value={newContent} onChange={(e) => setNewContent(e.target.value)}></textarea>
      <button onClick={addNewBlog}>Add Blog</button>
    </div>
  );
}

export default NewBlogForm;
