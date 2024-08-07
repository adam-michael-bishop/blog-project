import { Box, Grid, Button, Typography} from '@mui/material'
import { useDispatch } from 'react-redux'
import { toggleThemeMode } from '../state/themeModeSlice';
import { Link } from 'react-router-dom';

function Navbar() {
    const dispatch = useDispatch();

    return (
        <Box sx={{height: '10vh', backgroundColor: '', overflow: 'hidden'}}>
            <Grid 
                sx={{padding: '.5em'}}
                columns={12}
                container={true}
                direction={'row'}
                justifyContent={'space-between'}
            >
                <Button size='medium' variant='contained'>Burger</Button>
                <Link to={'/'}>Home</Link>
                <Link to={'about'}>About</Link>
                <Button onClick={() => {dispatch(toggleThemeMode())}}>theme</Button>
                <Typography>Logo</Typography>
            </Grid>
        </Box>
    )
}

export default Navbar