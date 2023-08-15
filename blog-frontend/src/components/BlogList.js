import React, { useState } from 'react';
import './BlogList.css';

function BlogList({ blogs, updateBlog }) {
  const [editingBlogId, setEditingBlogId] = useState(null);
  const [editedTitle, setEditedTitle] = useState('');
  const [editedContent, setEditedContent] = useState('');

  const handleEditClick = (blog) => {
    setEditingBlogId(blog.id);
    setEditedTitle(blog.title);
    setEditedContent(blog.content);
  };

  const handleDoneEditingClick = (blogId) => {
    updateBlog(blogId, editedTitle, editedContent);
    setEditingBlogId(null);
  };

  return (
    <>
      {blogs.map(blog => (
        <div key={blog.id} className="blog-container">
          <div className="blog-content">
            {editingBlogId === blog.id ? (
              <>
                <input
                  className="edited-title"
                  type="text"
                  value={editedTitle}
                  onChange={e => setEditedTitle(e.target.value)}
                />
                <textarea
                  className="editing-content"
                  value={editedContent}
                  onChange={e => setEditedContent(e.target.value)}
                />
              </>
            ) : (
              <>
                <h2>{blog.title}</h2>
                <p>{blog.content}</p>
              </>
            )}
          </div>
          <div className="blog-options">
            {editingBlogId === blog.id ? (
              <button
              className="blog-button done-editing-button"
              onClick={() => handleDoneEditingClick(blog.id)}>Done Editing
              </button>
            ) : (
              <>
                <button className="blog-button edit-button" onClick={() => handleEditClick(blog)}>Edit</button>
                <button className="blog-button delete-button">Delete</button>
                <button className="blog-button copy-button">Copy</button>
              </>
            )}
          </div>
        </div>
      ))}
    </>
  );
}

export default BlogList;
