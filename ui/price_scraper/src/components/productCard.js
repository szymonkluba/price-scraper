import React from "react";
import ProductDetails from "./productDetails";

class ProductCard extends React.Component {
    render() {
        const details = {
            current_prices: this.props.product.current_prices,
            name: this.props.product.name,
            url: this.props.product.url,
            category: this.props.product.category,
            price: this.props.product.price,
            timestamp: this.props.product.timestamp,
            available: this.props.product.available,
            image_url: this.props.product.image_url,
        }

        return (
            <div className={'product-card'}>
                <ProductDetails details={details} />
            </div>
        );
    }
}

export default ProductCard