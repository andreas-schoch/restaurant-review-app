import { combineReducers } from "redux";
import { tokenReducer } from "./tokenReducer";
import { restaurantReducer } from "./restaurantReducer";
import { commentReducer } from "./commentReducer";
import { userReducer } from "./userReducer";
import { meReducer } from "./meReducer";
import { loginReducer } from "./loginReducer";

export const reducers = combineReducers({
    tokenReducer,
    restaurantReducer,
    commentReducer,
    userReducer,
    meReducer,
    loginReducer
    
});
