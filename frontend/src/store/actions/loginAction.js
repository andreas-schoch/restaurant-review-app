import axios from "axios";
import { ERROR, LOGIN, LOGOUT } from "../types";

const URL = `https://jable.co/`;

export const login = (token, refresh) => {
  return {
    type: LOGIN,
    token: token,
    refresh: refresh
  };
};

const error = error => {
  return {
    type: ERROR,
    payload: error
  };
};

export const logout = () => {
  return {
    type: LOGOUT
  };
};

export const loginAction = ({ username, password }) => async dispatch => {
  try {
    // console.log(username);
    const response = await axios.post(`${URL}api/token/`, {
      username,
      password
    });
    const token = response.data.access;
    const refresh = response.data.refresh;
    localStorage.setItem("token", token);
    localStorage.setItem("refresh", refresh);
    dispatch(login(token, refresh));
    return response;
  } catch (e) {
    dispatch(error("Wrong username or password"));
  }
};

export const refreshAction = token => async dispatch => {
  const body = {
    refresh: token
  };

  try {
    // console.log(username);
    const response = await axios.post(`${URL}/api/token/refresh`, body);
    const token = response.data.access;
    console.log(token);
    localStorage.setItem("token", token);
    dispatch(login(token));
    return response;
  } catch (e) {
    dispatch(error("something"));
  }
};
