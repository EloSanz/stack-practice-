import express, { Request, Response, Express } from 'express';

const app: Express = express();
const PORT = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Endpoint GET: Obtiene posts desde la API externa
app.get('/api/postsss/:id', async (req: Request, res: Response) => {
    try {
        console.log('Fetching posts from external APIIII...');
        const apiResponse = await fetch(`https://jsonplaceholder.typicode.com/posts/${req.params.id}`);

        if (!apiResponse.ok) {
            throw new Error(`External API error: ${apiResponse.status}`);
        }

        const data = await apiResponse.json();
        res.json(data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Endpoint POST: Crea un post en la API externa
app.post('/api/posts', async (req: Request, res: Response) => {
    try {
        console.log('Creating post on external API...', req.body);
        const apiResponse = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(req.body),
        });

        const data = await apiResponse.json();
        res.status(201).json(data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(PORT, () => { console.log(`🚀 Server running on http://localhost:${PORT}`); });
