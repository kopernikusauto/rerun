use re_types::{
    archetypes::Asset3D,
    components::{Blob, MediaType},
    datatypes::Utf8,
    Archetype as _, AsComponents as _,
};

#[test]
fn roundtrip() {
    const BYTES: &[u8] = &[1, 2, 3, 4, 5, 6];

    let expected = Asset3D {
        blob: Blob(BYTES.to_vec().into()),
        media_type: Some(MediaType(Utf8(MediaType::GLTF.into()))),
        out_of_tree_transform: Some(re_types::components::OutOfTreeTransform::ENABLED),
    };

    let arch = Asset3D::from_file_contents(BYTES.to_vec(), Some(MediaType::gltf()))
        .with_out_of_tree_transform(true);
    similar_asserts::assert_eq!(expected, arch);

    // let expected_extensions: HashMap<_, _> = [
    // ]
    // .into();

    eprintln!("arch = {arch:#?}");
    let serialized = arch.to_arrow().unwrap();
    for (field, array) in &serialized {
        // NOTE: Keep those around please, very useful when debugging.
        // eprintln!("field = {field:#?}");
        // eprintln!("array = {array:#?}");
        eprintln!("{} = {array:#?}", field.name);

        // TODO(cmc): Re-enable extensions and these assertions once `arrow2-convert`
        // has been fully replaced.
        // util::assert_extensions(
        //     &**array,
        //     expected_extensions[field.name.as_str()].as_slice(),
        // );
    }

    let deserialized = Asset3D::from_arrow(serialized).unwrap();
    similar_asserts::assert_eq!(expected, deserialized);
}

mod util;
