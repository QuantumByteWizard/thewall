<script lang="ts">
    import { onMount } from 'svelte';
    import { fetchPosts, type Post } from '$lib/api';
    import PostCard from '$lib/components/PostCard.svelte';
    import CreatePostForm from '$lib/components/CreatePostForm.svelte';

    let posts: Post[] = [];
    let showModal = false;

    async function loadPosts() {
        try {
            posts = await fetchPosts();
        } catch (e) {
            console.error(e);
        }
    }

    onMount(() => {
        loadPosts();
    });

    function handlePostCreated(event: CustomEvent<Post>) {
        posts = [event.detail, ...posts];
        showModal = false;
    }
</script>

<div class="wall-container">
    <header>
        <h1>The Wall</h1>
        <button class="add-btn" on:click={() => showModal = true}>+ Add Note</button>
    </header>

    <div class="wall">
        {#each posts as post (post.id)}
            <div class="post-wrapper">
                <PostCard {post} />
            </div>
        {/each}
        {#if posts.length === 0}
            <div class="empty-state">
                <p>The wall is empty. Be the first to post!</p>
            </div>
        {/if}
    </div>

    {#if showModal}
        <div class="modal-backdrop" on:click={() => showModal = false}>
            <div class="modal-content" on:click|stopPropagation>
                <div class="modal-header">
                    <button class="close-btn" on:click={() => showModal = false}>×</button>
                </div>
                <CreatePostForm on:created={handlePostCreated} />
            </div>
        </div>
    {/if}
</div>

<style>
    .wall-container {
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }

    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
        border-bottom: 2px solid #ddd;
        padding-bottom: 20px;
    }

    h1 {
        font-size: 2.5rem;
        margin: 0;
        letter-spacing: -1px;
    }

    .add-btn {
        background: #333;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 1rem;
        cursor: pointer;
        transition: transform 0.1s;
    }

    .add-btn:hover {
        transform: scale(1.05);
    }

    .wall {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 30px;
        padding-bottom: 50px;
    }

    .empty-state {
        grid-column: 1 / -1;
        text-align: center;
        padding: 50px;
        color: #888;
        font-size: 1.2rem;
    }

    /* Modal Styles */
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 100;
        backdrop-filter: blur(2px);
    }

    .modal-content {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        width: 90%;
        max-width: 450px;
        position: relative;
    }

    .modal-header {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 10px;
    }

    .close-btn {
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0 5px;
        line-height: 1;
    }
</style>
