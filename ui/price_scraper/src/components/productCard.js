import React from "react";
import Thumbnail from "./thumbnail";
import ProductDetails from "./productDetails";
import ThumbnailPlaceholder from "./thumbnailPlaceholder";

class ProductCard extends React.Component {
    render() {
        const details = {
            current_prices: this.props.product.current_prices,
            name: this.props.product.name,
            url: this.props.product.url,
            category: this.props.product.category
        }

        return (
            <div className={'product-card'}>
                <ProductDetails details={details} />
            </div>
        );
    }
}

export default ProductCard