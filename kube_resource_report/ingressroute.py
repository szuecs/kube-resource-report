from pykube.objects import NamespacedAPIObject


class IngressRoute(NamespacedAPIObject):

    """
    Kubernetes API objct for IngressRoute.

    See https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/
    """

    version = "traefik.containo.us/v1alpha1"
    kind = "IngressRoute"
    endpoint = "ingressroutes"
