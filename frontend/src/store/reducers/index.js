import { combineReducers } from "redux";
import { tokenReducer } from "./tokenReducer";
import { restaurantReducer } from "./restaurantReducer";
import { commentReducer } from "./commentReducer";
import { userReducer } from "./userReducer";

export const reducers = combineReducers({
    'tokens': tokenReducer,
    'restaurants': restaurantReducer,
    'comments': commentReducer,
    'users': userReducer,
});
