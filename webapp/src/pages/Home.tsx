import { Container, Typography } from '@mui/material'
import { BlogPost } from '../types/types';
import Feed from '../components/Feed';

//Example blog posts
const blogPosts: BlogPost[] = [
    {
      id: 1,
      title: 'Understanding React Hooks',
      excerpt: 'React hooks have transformed the way we build components...',
      date: 'August 7, 2024',
      avatar: 'A'
    },
    {
      id: 2,
      title: 'JavaScript ES2024 Features',
      excerpt: 'Let\'s explore the new features introduced in ES2024...',
      date: 'August 5, 2024',
      avatar: 'B'
    },
    {
      id: 3,
      title: 'A Guide to CSS Flexbox',
      excerpt: 'Flexbox is a powerful layout module that provides...',
      date: 'August 3, 2024',
      avatar: 'C'
    },
  ];

export default function Home() {
  return (
    <Container>
        <Typography variant='h1' sx={{textAlign: 'center'}}>Blog Home</Typography>
        <Feed posts={blogPosts} />
    </Container>
  )
}