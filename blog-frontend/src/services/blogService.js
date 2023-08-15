const baseURL = "https://teds-blogs-9c73db19cf47.herokuapp.com/api/blogs";

export const fetchBlogs = () => {
  return fetch(baseURL)
    .then(res => {
      if (!res.ok) {
        throw new Error(`Server responded with status: ${res.status}`);
      }
      return res.json();
    });
}

export const addBlog = (title, content) => {
  return fetch(baseURL, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title,
      content
    })
  }).then(res => res.json());
}

export const updateBlogInAPI = (id, title, content) => {
  return fetch(`${baseURL}/${id}`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title,
      content
    })
  }).then(res => {
    if (!res.ok) {
      throw new Error(`Server responded with status: ${res.status}`);
    }
    return res.json();
  });
}
