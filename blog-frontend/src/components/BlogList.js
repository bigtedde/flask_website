import React from 'react';

function BlogList({ blogs }) {
  return (
    <>
      {blogs.map(blog => (
        <div key={blog.id}>
          <h2>{blog.title}</h2>
          <p>{blog.content}</p>
        </div>
      ))}
    </>
  );
}

export default BlogList;
