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
            return <div className={'picker show'}>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div className={'picker show'}>Loading...</div>;
        } else {
            return (
                <div id='picker' className={'picker show'}>
                    <ul className={'picker-items'}>
                        {items.map((link) => {
                            return (
                            <li key={link.slug}>
                                <Link className={"menu-item"} to={link.products}>{link.name}</Link>
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