// import { API_URL } from "../constants";
import { useEffect, useState} from 'react'
import axios from 'axios'
import { type } from '@testing-library/user-event/dist/type';
function getlist() {
    
}



export default function Teamlist() {
    const [catUrl, setCatUrl] = useState('');
    const [error, setError] = useState(false);
    const [state, setState] = useState('');
    useEffect(() => {
        setState('loading');
        axios
            .get('https://jsonplaceholder.typicode.com/users/1')
            .then((res) => {
                console.log(res);
                //console.log(typeof JSON.stringify(res))
                setState('success');
                setCatUrl(res.data);
            })
            .catch((err) => {
                console.error('Error:', err);
                setState('error');
                setError(err);
            });
    }, []);
    if (state === 'error')
        return (
            <h1>

                {error.toString()}
            </h1>
        );
    
    const listItems = 'catUrl';
    return (
        <div>
            <div>
                {state === 'loading' ? (
                    <h1>Loading...</h1>
                ) : (
                    listItems
                )}
            </div>
            {/* {catUrl.map(home => <div>{home.name}</div>)} */}
                    
        </div>
    );
}