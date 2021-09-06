import React from "react";
import {Link} from "react-router-dom";

class Picker extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            previous: null,
            next: null,
            count: null
        }
    }

    componentDidMount() {
        fetch(this.props.url)
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result);
                    this.setState({
                        visible: false,
                        isLoaded: true,
                        items: result.results,
                        previous: result.previous,
                        next: result.next,
                        count: result.count
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )

    }

    render() {

        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className={'picker'}>
                    <ul className={'picker-items'}>
                        {items.map((link) => {
                            return (
                            <li key={link.slug}>
                                <Link to={link.products}>{link.name}</Link>
                            </li>
                            )
                        })}
                    </ul>
                </div>
            )
        }

    }
}

export default Picker