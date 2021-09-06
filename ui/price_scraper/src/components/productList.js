import React from "react";
import ProductCard from "./productCard";
import {withRouter} from "react-router-dom";

class ProductList extends React.Component {
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
        const location = this.props.location.pathname === '/' ? '/products/' : this.props.location.pathname;
        console.log(location)
        const path = window.location.origin.replace('3000', '8000') + location;
        console.log(path)
        this.fetchProducts(path);
    }

    fetchProducts(path) {
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
            return items.map((product) => <ProductCard key={product.slug}
                                                       product={product}/>);
        }
    }
}

export default withRouter(ProductList)