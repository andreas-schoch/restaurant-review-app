import { ERROR, LOGIN, LOGOUT, REFRESH } from "../types";
const initialState = {};

export const loginReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOGIN: {
      return {
        ...state,
        token: action.token,
        refresh: action.refresh,
        error: null,
        authenticated: true
      };
    }
    case ERROR: {
      return {
        ...state,
        token: null,
        error: action.payload,
        authenticated: false
      };
    }
    case LOGOUT: {
      localStorage.removeItem("token");
      return { ...state, token: null, error: null, authenticated: false };
    }
    case REFRESH: {
      localStorage.clear();
      return { ...state, token: null, error: null, authenticated: false };
    }
    default:
      return state;
  }
};
