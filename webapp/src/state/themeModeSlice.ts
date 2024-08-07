import { PaletteMode } from "@mui/material";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const LIGHT = 'light';
const DARK = 'dark';

export interface ThemeModeState {
    mode: PaletteMode | undefined;
}

const initialState: ThemeModeState = {
    mode: undefined,
}

const themeModeSlice = createSlice({
    name: "themeMode",
    initialState,
    reducers: {
        toggleThemeMode: (state) => {
            state.mode = state.mode === LIGHT ? DARK : LIGHT;
        },
        setThemeMode: (state, action: PayloadAction<PaletteMode | undefined>) => {
            state.mode = action.payload;
        }
    },
});

export const { toggleThemeMode, setThemeMode } = themeModeSlice.actions;
export default themeModeSlice.reducer;