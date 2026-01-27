interface Post {
    userId: number;
    id: number;
    title: string;
    body: string;
}


// 1. Ejemplo GET (Equivalente a curl -X GET url)
async function getPost() {
    try {
        const response: Response = await fetch('https://jsonplaceholder.typicode.com/posts/1');

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const data = (await response.json()) as Post;
        console.log('--- GET Response ---');
        console.log(data);
    } catch (error) {
        console.error('Failed to fetch post:', error);
    }
}

// 2. Ejemplo POST (Equivalente a curl -X POST -d '...' url)
async function createPost() {
    try {
        const response: Response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: 'foo',
                body: 'bar',
                userId: 1,
            }),
        });

        const data = await response.json();
        console.log('\n--- POST Response ---');
        console.log(data);
    } catch (error) {
        console.error('Failed to create post:', error);
    }
}

// Ejecutar las funciones
(async () => {
    await getPost();
    await createPost();
})();
