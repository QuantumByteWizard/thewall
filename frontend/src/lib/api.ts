export interface Post {
    id: number;
    content: string;
    timestamp: string;
    color: string;
    rotation: number;
}

const API_URL = 'http://localhost:8000'; // Update for production

export async function fetchPosts(skip = 0, limit = 100): Promise<Post[]> {
    const response = await fetch(`${API_URL}/posts?skip=${skip}&limit=${limit}`);
    if (!response.ok) {
        throw new Error('Failed to fetch posts');
    }
    return response.json();
}

export async function createPost(content: string, color: string = '#ffffff'): Promise<Post> {
    const rotation = Math.floor(Math.random() * 10) - 5; // Random rotation between -5 and 5 degrees
    const response = await fetch(`${API_URL}/posts`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content, color, rotation }),
    });
    if (!response.ok) {
        throw new Error('Failed to create post');
    }
    return response.json();
}
