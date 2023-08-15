import './BlogList.css';
import React from 'react';

function BlogList({ blogs }) {
  return (
    <>
      {blogs.map(blog => (
        <div key={blog.id} className="blog-container">
          <div className="blog-content">
            <h2>{blog.title}</h2>
            <p>{blog.content}</p>
          </div>
          <div className="blog-options">
            <button className="blog-button edit-button">Edit</button>
            <button className="blog-button delete-button">Delete</button>
            <button className="blog-button copy-button">Copy</button>
          </div>
        </div>
      ))}
    </>
  );
}

export default BlogList;
