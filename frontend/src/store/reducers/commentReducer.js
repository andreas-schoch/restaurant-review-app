import { COMMENTS } from "../types";
const initialState = {};

export const commentReducer = (state = initialState, action) => {
  switch (action.type) {
    case COMMENTS: {
      return { ...state, comments: action.payload };
    }
    default:
      return state;
  }
};

