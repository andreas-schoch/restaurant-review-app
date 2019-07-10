import { ME } from "../types";
const initialState = {};

export const meReducer = (state = initialState, action) => {
  switch (action.type) {
    case ME: {
      return { ...state, me: action.payload };
    }
    default:
      return state;
  }
};