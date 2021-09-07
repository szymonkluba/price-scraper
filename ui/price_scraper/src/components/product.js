import React from "react";
import ProductCard from "./productCard";
import PricesHistory from "./pricesHistory";


class Product extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            product: null,
        };
    }

    componentDidMount() {
        const location = this.props.location.pathname === '/' ? '/products/' : this.props.location.pathname;
        const path = window.location.origin.replace('3000', '8000') + location;
        this.fetchProduct(path)
    }

    fetchProduct(path) {
        fetch(path)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        product: result,
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
        const {error, isLoaded, product} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            const url = window.location.origin.replace('3000', '8000') + '/prices/?product=' + product.slug;
            return (
                <div>
                    <ProductCard key={product.slug} product={product} />
                    <PricesHistory key={product.slug + "-prices"} url={url} />
                </div>
            )
        }
    }
}

export default Product;