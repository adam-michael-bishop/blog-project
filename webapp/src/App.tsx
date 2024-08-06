import { Box, Button, Grid, Typography } from '@mui/material'
import './App.css'

function App() {
  return (
    <Box sx={{width: '100vw', height: '100vh'}}>
      <Box sx={{height: '10vh', backgroundColor: 'gray', overflow: 'hidden'}}>
        <Grid sx={{padding: '.5em'}} columns={12} display={'flex'} direction={'row'}>
          <Box >
            <Button size='medium' variant='contained'>Sidebar</Button>
          </Box>
          <Box >
            <Typography>Logo</Typography>
          </Box>
        </Grid>
      </Box>
    </Box>
  )
}

export default App
