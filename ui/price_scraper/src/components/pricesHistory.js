import React from "react";
import ProductCard from "./productCard";
import PriceTag from "./priceTag";

class PricesHistory extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            previous: null,
            next: null,
            count: null
        };
    }

    componentDidMount() {
        this.fetchPrices(this.props.url)
    }

    fetchPrices(path) {
        fetch(path)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
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
                <div>
                    {items.map((price) => <PriceTag key={price.slug + price.timestamp}
                                                    price={price}/>)}
                </div>
            )
        }
    }
}

export default PricesHistory;