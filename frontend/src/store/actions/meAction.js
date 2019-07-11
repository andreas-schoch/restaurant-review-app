import axios from "axios";
import { ME } from "../types";
const URL = `https://jable.co/api/`;

export const me = data => {
  return {
    type: ME,
    payload: data
  };
};
export const getMe = () => async (dispatch, getState) => {
    console.log(getState().tokens)
  const token = getState().tokens.token;
  const config = {
    headers: {
      Authorization: `Bearer ${token}`
    }
  };
  const response = await axios.get(`${URL}users/me`, config);
  const data = response.data;
  dispatch(me(data));
};
