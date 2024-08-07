import React from 'react'
import { List, ListItem, ListItemText, Typography, Divider} from '@mui/material'
import { BlogPost } from '../types/types';

type FeedProps = {
    posts: BlogPost[];
}

function Feed({ posts } : FeedProps ) {
    return (
        <List>
          {posts.map((post) => (
            <React.Fragment key={post.id}>
              <ListItem alignItems="flex-start">
                <ListItemText
                  primary={
                    <Typography variant="h6" component="h2">
                      {post.title}
                    </Typography>
                  }
                  secondary={
                    <>
                      <Typography
                        component="span"
                        variant="body2"
                      >
                        {post.date}
                      </Typography>
                      {' — '}
                      {post.excerpt}
                    </>
                  }
                />
              </ListItem>
              <Divider component="li" />
            </React.Fragment>
          ))}
        </List>
      );    
}

export default Feed