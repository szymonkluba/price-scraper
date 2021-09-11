import React from "react";
import {Link} from "react-router-dom";
import SplashScreen from "./splashScreen";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faChevronCircleRight} from "@fortawesome/free-solid-svg-icons";

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
        this.handleClick = this.handleClick.bind(this)
    }

    handleClick() {
        this.props.onItemClick(false)
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
            return (
                <div className={"picker show"}
                     style={{height: '40px'}}>
                    <SplashScreen className={"picker show"}/>
                </div>
            );
        } else {
            return (
                <div id='picker'
                     className={'picker'}>
                    <ul className={'picker-items'}>
                        {items.map((link) => {
                            return (
                                <li key={link.slug}>
                                    <Link onClick={this.handleClick}
                                          className={"picker-item"}
                                          to={link.products}>
                                        <span>
                                            <FontAwesomeIcon icon={faChevronCircleRight}/>
                                        </span>
                                        {link.name}
                                    </Link>
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