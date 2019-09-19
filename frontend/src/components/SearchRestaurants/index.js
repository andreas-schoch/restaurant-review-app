import React, {useEffect} from 'react';
import './index.scss';
import GenericRestaurantList from '../GenericRestaurantList';
import { connect } from 'react-redux' 
import { saveRestaurantsAction } from '../../store/actions/restaurantAction';


const SearchRestaurants = (props) =>  {
    useEffect(() => {
        const makeTheRequest = async () => {
            const data = await props.dispatch(saveRestaurantsAction());
            console.log("data", data);
        }
        console.log("useeffect called search restaurants");
        // makeTheRequest();
    }, []);

    return (
        <div className='search-restaurant-list'>
            <GenericRestaurantList restaurants={ props.restaurants }/>
        </div>
    );
};

const mapStateToProps = (state, ownProps) => {
    const objToArr = (obj) => Object.values(obj).map(item => item);
    return { 
        "restaurants": objToArr(state.restaurantReducer)
    };
};

export default connect(mapStateToProps)(SearchRestaurants);