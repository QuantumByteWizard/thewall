<script lang="ts">
    import type { Post } from '$lib/api';
    
    export let post: Post;

    function formatDate(dateString: string) {
        const date = new Date(dateString);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
</script>

<div class="post-card" style="background-color: {post.color}; transform: rotate({post.rotation}deg);">
    <p class="content">{post.content}</p>
    <div class="footer">
        <span class="timestamp">{formatDate(post.timestamp)}</span>
    </div>
</div>

<style>
    .post-card {
        padding: 20px;
        width: 250px;
        min-height: 200px;
        box-shadow: 2px 4px 8px rgba(0,0,0,0.2);
        border-radius: 4px; /* Slight rounding for sticky note feel */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s ease;
        color: #333;
        font-family: 'Kalam', cursive, sans-serif; /* Handwritten font feel if available, else fallback */
    }

    .post-card:hover {
        transform: scale(1.05) rotate(0deg) !important;
        z-index: 10;
        box-shadow: 4px 8px 12px rgba(0,0,0,0.3);
    }

    .content {
        font-size: 1.1rem;
        line-height: 1.4;
        white-space: pre-wrap;
    }

    .footer {
        margin-top: 15px;
        font-size: 0.8rem;
        opacity: 0.7;
        text-align: right;
    }
</style>
