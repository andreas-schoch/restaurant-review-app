import React, { useState } from 'react';
import './index.css';


const UserProfile = (props) =>  {
    return (
        <div>
            <div>
                {/* left section */}
                <img className='profile-picture-me' src="./assets/img/default-profile-picture.jpg" alt="" />
            </div>
        </div>
    )
}

export default UserProfile;