import React from "react";

class ThumbnailPlaceholder extends React.Component {
    render() {
        return (
            <div className={"image"}>
                <img src={process.env.PUBLIC_URL + '/img/product-image-placeholder-300x300.jpg'} alt={'Placeholder'}/>
            </div>
        )
    }
}

export default ThumbnailPlaceholder