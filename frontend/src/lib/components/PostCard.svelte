<script lang="ts">
    import type { Post } from '$lib/api';
    import { reactToPost } from '$lib/api';
    
    export let post: Post;
    let isReacting = false;

    function formatDate(dateString: string) {
        const date = new Date(dateString);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    async function handleReaction() {
        if (isReacting) return;
        isReacting = true;
        try {
            const result = await reactToPost(post.id);
            post.reactions = result.reactions;
        } catch (e) {
            console.error('Failed to react:', e);
        } finally {
            isReacting = false;
        }
    }
</script>

<div class="post-card" style="background-color: {post.color}; transform: rotate({post.rotation}deg);">
    <p class="content">{post.content}</p>
    <div class="footer">
        <span class="username">~ {post.username}</span>
        <div class="actions">
            <button class="heart-btn" on:click|stopPropagation={handleReaction} disabled={isReacting} aria-label="Like post" class:liked={post.reactions > 0}>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="heart-icon">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
                <span class="count">{post.reactions || 0}</span>
            </button>
        </div>
    </div>
    <div class="timestamp-row">
        <span class="timestamp">{formatDate(post.timestamp)}</span>
    </div>
</div>

<style>
    .post-card {
        padding: 20px;
        width: 250px;
        min-height: 200px;
        box-shadow: 2px 4px 8px rgba(0,0,0,0.2);
        border-radius: 4px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s ease;
        color: #333;
        font-family: 'Kalam', cursive, sans-serif;
        cursor: default;
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
        margin-bottom: auto; /* Push footer down */
    }

    .footer {
        margin-top: 15px;
        font-size: 0.8rem;
        opacity: 0.9;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .username {
        font-weight: bold;
        font-style: italic;
        opacity: 0.7;
    }

    .actions {
        display: flex;
        align-items: center;
    }

    .heart-btn {
        background: none;
        border: none;
        cursor: pointer;
        padding: 5px;
        border-radius: 50%;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 5px;
        color: #555;
    }

    .heart-icon {
        transition: all 0.2s;
        fill: transparent;
        stroke: #555;
    }

    .heart-btn:hover {
        transform: scale(1.1);
        background: rgba(0,0,0,0.05);
    }

    .heart-btn:hover .heart-icon {
        stroke: #e74c3c;
    }
    
    .heart-btn.liked .heart-icon {
        fill: #e74c3c;
        stroke: #e74c3c;
    }

    .heart-btn:active {
        transform: scale(0.9);
    }

    .count {
        font-size: 0.9rem;
        font-weight: bold;
    }

    .timestamp-row {
        text-align: right;
        margin-top: 5px;
    }

    .timestamp {
        font-size: 0.7rem;
        opacity: 0.5;
    }
</style>
