import './BlogList.css';
import React, { useState } from 'react';

function BlogList({ blogs }) {
  const [shownOptionsBlogId, setShownOptionsBlogId] = useState(null);

  return (
    <>
      {blogs.map(blog => (
        <div key={blog.id} className="blog-container">
          <div className="blog-content">
            <h2>{blog.title}</h2>
            <p>{blog.content}</p>
          </div>
          <div className="blog-options">
            <button onClick={() => setShownOptionsBlogId(blog.id)}>Options</button>
            {shownOptionsBlogId === blog.id && (
              <ul className="options-menu">
                <li>Remove</li>
                <li>Delete</li>
              </ul>
            )}
          </div>
        </div>
      ))}
    </>
  );
}

export default BlogList;
