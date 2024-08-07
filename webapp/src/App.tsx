import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Box, CssBaseline } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material';
import useMediaQuery from '@mui/material/useMediaQuery';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from './state/store';
import { useMemo } from 'react';
import './App.css';

/* Page Imports */
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import { setThemeMode } from './state/themeModeSlice';


function App() {
  const mode = useSelector((state: RootState) => state.themeMode.mode);
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');
  const dispatch = useDispatch();

  if (prefersDarkMode && mode === undefined) {
    dispatch(setThemeMode('dark'))
  }

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: mode,
        },
      }),
    [mode],
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Box sx={{width: '100vw', height: '100vh'}}>
          <Navbar />
          <Routes>
            <Route path='/' element={<Home />}/>
            <Route path='about' element={<About />}/>
          </Routes>
        </Box>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default App
