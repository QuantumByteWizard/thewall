<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { createPost } from '$lib/api';

    const dispatch = createEventDispatcher();

    let content = '';
    let color = '#fff740'; // Default yellow
    let isSubmitting = false;
    let error = '';

    const colors = [
        '#fff740', // Yellow
        '#ff7eb9', // Pink
        '#7afcff', // Blue
        '#feff9c', // Light Yellow
        '#fff6ff', // Whiteish
        '#98ff98', // Mint
    ];

    async function handleSubmit() {
        if (!content.trim()) return;
        
        isSubmitting = true;
        error = '';

        try {
            const newPost = await createPost(content, color);
            dispatch('created', newPost);
            content = ''; // Reset form
        } catch (e) {
            error = 'Failed to post. Please try again.';
        } finally {
            isSubmitting = false;
        }
    }
</script>

<div class="form-container">
    <h3>Write a positive note</h3>
    
    <textarea 
        bind:value={content} 
        placeholder="Share something positive..." 
        maxlength="500"
        disabled={isSubmitting}
    ></textarea>
    
    <div class="controls">
        <div class="color-picker">
            {#each colors as c}
                <button 
                    class="color-dot {color === c ? 'selected' : ''}" 
                    style="background-color: {c};"
                    on:click={() => color = c}
                    aria-label="Select color"
                ></button>
            {/each}
        </div>
        
        <button class="submit-btn" on:click={handleSubmit} disabled={isSubmitting || !content.trim()}>
            {isSubmitting ? 'Posting...' : 'Post'}
        </button>
    </div>

    {#if error}
        <p class="error">{error}</p>
    {/if}
</div>

<style>
    .form-container {
        background: white;
        padding: 20px;
        border-radius: 8px;
        width: 100%;
        max-width: 400px;
    }

    h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #333;
    }

    textarea {
        width: 100%;
        height: 120px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        resize: vertical;
        font-family: inherit;
        font-size: 1rem;
        margin-bottom: 15px;
    }

    .controls {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .color-picker {
        display: flex;
        gap: 8px;
    }

    .color-dot {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 1px solid #ddd;
        cursor: pointer;
        transition: transform 0.1s;
    }

    .color-dot:hover {
        transform: scale(1.1);
    }

    .color-dot.selected {
        border: 2px solid #333;
        transform: scale(1.1);
    }

    .submit-btn {
        background: #333;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
    }

    .submit-btn:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }

    .error {
        color: red;
        margin-top: 10px;
        font-size: 0.9rem;
    }
</style>
