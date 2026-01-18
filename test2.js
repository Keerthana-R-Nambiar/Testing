const express = require("express");
const app = express();

app.use(express.urlencoded({ extended: true }));

// ❌ Broken Access Control
app.get("/admin", (req, res) => {
    res.send("Welcome Admin! You have full access.");
});

// ❌ XSS Vulnerability
app.get("/search", (req, res) => {
    const query = req.query.q;
    res.send(`<h1>Search Results for ${query}</h1>`);
});

// ❌ Client-controlled redirect (Open Redirect)
app.get("/redirect", (req, res) => {
    res.redirect(req.query.url);
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
