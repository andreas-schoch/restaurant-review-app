import { ADD_TOKENS, REFRESH_TOKEN } from "../types";
import axios from 'axios'

// TODO insert backend url when available and store it on a single place
const url = '';


const login = (tokens) => {
    return {
        type: ADD_TOKENS,
        payload: { tokens }
    }
};


export const loginAction = (username, password) => async (dispatch, getState) => {
    try {
        const res = await axios.post(`${ URL }/api/auth/token/`, { username, password });

        const tokens = { access: res.data.access, refresh: res.data.refresh};
        localStorage.setItem('tokens', tokens);

        dispatch(login(tokens));
        return tokens;
    } catch (e) {
        console.error('user does not exist'); // TODO change to error object
    }
};
